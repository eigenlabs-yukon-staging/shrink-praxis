#!/usr/bin/env python3
"""Check a parameter file and write the manifest that declares it. Standard library only.

Run from the repository root:

  python3 tools/pack.py            check submission/params.json with the protected model,
                                   print what the hosted gate will answer, and write
                                   submission/submission.json
  python3 tools/pack.py --check    confirm that submission/submission.json declares exactly
                                   the text of submission/params.json (exit 0 or 1)
  python3 tools/pack.py --try FILE evaluate any parameter file and print the gate's answer;
                                   writes nothing (use it to search)

The manifest carries params.json to the protected gate as its own text, in parts of at most
4000 characters. The hosted evaluator allows a declared input of at most 16,384 bytes.
"""
import hashlib
import importlib.util
import json
from pathlib import Path
import sys

sys.dont_write_bytecode = True  # a __pycache__ directory must not end up in the repository

ROOT = Path(__file__).resolve().parent.parent
PARAMS = ROOT / "submission" / "params.json"
PROOF = ROOT / "submission" / "proof.md"
MANIFEST = ROOT / "submission" / "submission.json"
INPUT_LIMIT = 16384


def gate_module():
    spec = importlib.util.spec_from_file_location("praxis_gate", str(ROOT / "checkers" / "praxis_gate.py"))
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def canonical_size(value):
    return len(json.dumps(value, sort_keys=True, ensure_ascii=True, separators=(",", ":")))


def main(argv):
    gate = gate_module()
    if "--try" in argv:
        data = Path(argv[argv.index("--try") + 1]).read_bytes()
        print(json.dumps(gate.run({"params": gate.encode(data)}, root=ROOT), indent=1))
        return 0
    data = PARAMS.read_bytes()
    digest = hashlib.sha256(data).hexdigest()
    if "--check" in argv:
        manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
        declared = [c for c in manifest.get("checks", []) if c.get("check") == "praxis_gate"]
        same = len(declared) == 1 and gate.decode(declared[0]["inputs"]["params"]) == data
        print(("MATCH" if same else "MISMATCH") + ": submission.json declares "
              + ("exactly" if same else "something other than") + f" the text of params.json (sha256 {digest})")
        return 0 if same else 1
    inputs = {"params": gate.encode(data)}
    answer = gate.run(inputs, root=ROOT)
    print(json.dumps(answer, indent=1))
    packed = canonical_size(inputs)
    print(f"params.json: {len(data)} bytes, sha256 {digest}; declared input: {packed} of {INPUT_LIMIT} bytes")
    if packed > INPUT_LIMIT or len(inputs["params"]) > 8:
        print("NOT WRITTEN: params.json is larger than the hosted evaluator accepts. Use shorter rationals.")
        return 1
    if not answer["passed"]:
        print("NOT WRITTEN: the gate does not pass, so this submission would get no score.")
        return 1
    amended = answer["tier"] == "amended"
    if amended and not PROOF.exists():
        print("NOT WRITTEN: this submission amends the model, so submission/proof.md is required (rules.md).")
        return 1
    try:
        title = json.loads(data.decode("utf-8")).get("title") or "Parameters"
    except ValueError:
        title = "Parameters"
    changed = ", ".join(answer["amended"] + [f"drop {d}" for d in answer["dropped"]])
    claim = (f"params.json is a parameter set of Praxis for the reference statement at 100-bit security whose "
             f"ciphertext is {answer['ciphertext_mib']} MiB ({answer['gib']} GiB) and whose time, one encryption plus one expected "
             f"decryption, is {answer['time_mmul']} million field multiplications ({answer['enc_mmul']} and {answer['dec_mmul']}), "
             f"by the protected model, and ")
    if amended:
        claim += (f"every rule of the model as amended holds for it; proof.md proves that each amended entry "
                  f"({changed}) is sound, so that the paper's theorems hold for these parameters as rules.md requires.")
    else:
        claim += "every rule of the paper's own model holds for it: the paper's theorems apply to these parameters as stated."
    manifest = {
        "version": 1,
        "title": " ".join(str(title).split())[:300],
        "claims": [claim],
        "experiments": [],
        "checks": [{"check": "praxis_gate", "inputs": inputs}],
    }
    MANIFEST.write_text(json.dumps(manifest, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"wrote {MANIFEST.relative_to(ROOT)}: size {answer['ciphertext_mib']} MiB ({answer['gib']} GiB), time {answer['time_mmul']} M mul "
          f"(enc {answer['enc_mmul']}, dec {answer['dec_mmul']}), tier {answer['tier']}"
          + (f", amended: {changed}" if amended else ""))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
