# 🔑🔒 Cryptography in Python

[![Notebooks](https://img.shields.io/github/actions/workflow/status/jrafa1607/Cryptography_In_Python/notebooks.yml?label=Notebooks&style=for-the-badge&logo=githubactions&logoColor=white)](https://github.com/jrafa1607/Cryptography_In_Python/actions/workflows/notebooks.yml)
[![Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![cryptography](https://img.shields.io/badge/library-cryptography-2E7D32?style=for-the-badge)](https://cryptography.io/)
[![Google Colab](https://img.shields.io/badge/Run%20in-Colab-F9AB00?style=for-the-badge&logo=googlecolab&logoColor=white)](https://colab.research.google.com/github/jrafa1607/Cryptography_In_Python/)

*Hands-on notebooks on ciphers, hashes, and public-key cryptography, **and the attacks that break their weak uses**, each executed and verified automatically.*

---

#### 📓 Notebooks

All notebooks are in the [`Algorithms/`](Algorithms/) folder. Each one opens in **Google Colab** from the badge at its top, or you can browse them all in [Colab](https://colab.research.google.com/github/jrafa1607/Cryptography_In_Python/). `Runtime > Run all` works with no setup.

| Area | What is covered |
| --- | --- |
| Number theory | GCD, modular inverse, primality tests |
| Classical ciphers | Substitution, polyalphabetic, one-time pad |
| Block ciphers | Feistel networks, DES, AES, modes of operation |
| Hash functions | SHA-2, birthday attack, password hashing |
| Public-key | Factoring, discrete logarithm, elliptic curves |
| Attacks | Brute force, frequency analysis, key reuse |

---

#### ✅ Quality

| Check | How |
| --- | --- |
| Every notebook runs | CI executes all notebooks on each push and weekly |
| Results are verified | Each notebook asserts round trips and attack outcomes |
| Standard compliance | Known-answer tests (DES, secp256k1) |
| Secure randomness | Tests forbid `random` for key material |

To add a notebook, save it in `Algorithms/`: the CI finds and runs it automatically, with no list to update.<br>
To run locally: `pip install -r requirements.txt`, then `pytest --nbmake Algorithms/`.

> [!WARNING]
> The implementations are for learning. To protect real data, use a vetted library such as [`cryptography`](https://cryptography.io/) with authenticated encryption.

---

#### 📚 References

| Reference | Topic |
| --- | --- |
| [NIST SP 800-38A](https://csrc.nist.gov/pubs/sp/800/38/a/final) | Block cipher modes (ECB, CBC) |
| [NIST SP 800-38D](https://csrc.nist.gov/pubs/sp/800/38/d/final) | AES-GCM |
| [OWASP Password Storage](https://cheatsheetseries.owasp.org/cheatsheets/Password_Storage_Cheat_Sheet.html) | PBKDF2 iterations |
| [Handbook of Applied Cryptography](https://cacr.uwaterloo.ca/hac/) | ElGamal, Rabin, primality |

---

#### ⚖️ Intellectual Property (IP) Notice

All source code, documentation, and research methodologies contained in this repository are the exclusive Intellectual Property of the author. All rights reserved. Use of this content for academic or professional purposes must include proper citation and attribution (see [`CITATION.cff`](CITATION.cff)).

**Copyright © 2026 [João Rafael](https://www.linkedin.com/in/jrafa1607/).**
