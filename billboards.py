def strip_words(width, words):
    for i in range(1, len(words) + 1):
        line_text = ' '.join(words[:i])
        if len(line_text) > width:
            return words[i - 1:]
    return []

def word_too_wide(max_line_chars, words):
    word_lengths = map(len, words)
    return max(word_lengths) > max_line_chars

def text_fits(width, height, text, font_size):
    words = text.split()
    max_line_chars = width // font_size
    if word_too_wide(max_line_chars, words):
        return False

    lines = 0
    while words:
        lines += font_size
        words = strip_words(max_line_chars, words)
    return lines <= height


def bisect(low, high):
    return (low + high) // 2 


def search_font_size(width, height, text):
    current_font_size = high_font_size = height
    low_font_size = 0
    while True:
        if text_fits(width, height, text, current_font_size):
            low_font_size = current_font_size
            current_font_size = bisect(current_font_size, high_font_size)
            if low_font_size == current_font_size:
                return current_font_size
        else:
            high_font_size = current_font_size
            current_font_size = bisect(low_font_size, current_font_size)
            if high_font_size == current_font_size:
                return current_font_size


if __name__ == '__main__':
    pass
