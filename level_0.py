import re
import hashlib

def sanitize(text):
    p = re.compile(r"\w", re.UNICODE)
    return [(i, c.lower()) for i, c in enumerate(text) if p.match(c)]

def kgrams(text, k=5):
    return [text[i:i+k] for i in range(len(text) - k + 1)]

def winnowing_hash(kgram):
    text = "".join(c for _, c in kgram)
    hs = default_hash(text)
    return (kgram[0][0], hs)

def default_hash(text):
    hs = hashlib.sha1(text.encode("utf-8"))
    return int(hs.hexdigest()[-4:], 16)

def select_min(window):
    return min(window, key=lambda x: x[1])

def winnow(text, k=5):
    sanitized_text = sanitize(text)
    kgrams_list = list(kgrams(sanitized_text, k))
    hashes = [winnowing_hash(kg) for kg in kgrams_list]
    windows = list(kgrams(hashes, 4))
    fingerprints = set(map(select_min, windows))
    return fingerprints, kgrams_list

def compare_codes(code1, code2):
    fingerprints1, kgrams1 = winnow(code1)
    fingerprints2, kgrams2 = winnow(code2)
    common_fingerprints = fingerprints1.intersection(fingerprints2)
    common_lines = []

    for position, hash_value in common_fingerprints:
        line1 = next((line for line in kgrams1 if line[0][0] == position), None)
        line2 = next((line for line in kgrams2 if line[0][0] == position), None)
        if line1 and line2:
            common_lines.append((line1, line2))

    return common_fingerprints, common_lines