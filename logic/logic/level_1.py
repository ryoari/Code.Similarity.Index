import difflib

def normalized_levenshtein_distance(s1, s2):
    if len(s1) < len(s2):
        return normalized_levenshtein_distance(s2, s1)

    if len(s2) == 0:
        return 1.0

    previous_row = range(len(s2) + 1)
    for i, c1 in enumerate(s1):
        current_row = [i + 1]
        for j, c2 in enumerate(s2):
            insertions = previous_row[j + 1] + 1
            deletions = current_row[j] + 1
            substitutions = previous_row[j] + (c1 != c2)
            current_row.append(min(insertions, deletions, substitutions))
        previous_row = current_row
    
    distance = previous_row[-1]
    max_len = max(len(s1), len(s2))
    return 1 - (distance / max_len)

def compare_codes_level1(code1, code2, context_lines=3):
    lines1 = code1.splitlines()
    lines2 = code2.splitlines()
    
    # Use difflib to find matching blocks
    matcher = difflib.SequenceMatcher(None, lines1, lines2)
    matching_blocks = matcher.get_matching_blocks()
    
    detailed_similarity = []
    for match in matching_blocks:
        i, j, size = match
        if size > 0:
            # Extract the matching snippet and surrounding context
            start1 = max(0, i - context_lines)
            end1 = min(len(lines1), i + size + context_lines)
            start2 = max(0, j - context_lines)
            end2 = min(len(lines2), j + size + context_lines)
            
            snippet1 = '\n'.join(lines1[start1:end1])
            snippet2 = '\n'.join(lines2[start2:end2])
            
            similarity = normalized_levenshtein_distance(snippet1, snippet2)
            detailed_similarity.append((i, similarity, snippet1, snippet2))
    
    # Sort by similarity in descending order
    detailed_similarity.sort(key=lambda x: x[1], reverse=True)
    
    # Calculate overall similarity
    overall_similarity = sum(sim for _, sim, _, _ in detailed_similarity) / len(detailed_similarity) if detailed_similarity else 0
    
    return overall_similarity, detailed_similarity[:5]  # Return overall similarity and top 5 most similar snippets