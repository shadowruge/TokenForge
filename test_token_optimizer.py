from token_optimizer import TokenOptimizer


def test_clean_text_collapses_whitespace():
    opt = TokenOptimizer()
    assert opt.clean_text("texto   com    espacos\n\nsobrando") == "texto com espacos sobrando"


def test_clean_text_removes_html_tags():
    opt = TokenOptimizer()
    assert opt.clean_text("<p>oi <b>mundo</b></p>") == "oi mundo"


def test_clean_text_strips_edges():
    opt = TokenOptimizer()
    assert opt.clean_text("   texto com espaco nas bordas   ") == "texto com espaco nas bordas"


def test_compress_leaves_short_text_untouched():
    opt = TokenOptimizer()
    text = "texto curto"
    assert opt.compress(text) == text


def test_compress_truncates_long_text():
    opt = TokenOptimizer()
    text = "a" * 5000
    result = opt.compress(text)
    assert result.endswith("...")
    assert len(result) == opt.max_chars + 3


def test_summarize_keeps_first_three_sentences():
    opt = TokenOptimizer()
    text = "Um. Dois. Tres. Quatro. Cinco."
    assert opt.summarize(text) == "Um. Dois. Tres."


def test_optimize_auto_mode_returns_short_text_unchanged():
    opt = TokenOptimizer()
    assert opt.optimize("  pergunta   simples  ") == "pergunta simples"


def test_optimize_auto_mode_summarizes_long_text():
    opt = TokenOptimizer()
    text = ("frase. " * 2000)  # maior que max_chars
    result = opt.optimize(text, mode="auto")
    assert result == opt.summarize(opt.clean_text(text))


def test_optimize_compress_mode():
    opt = TokenOptimizer()
    text = "a" * 5000
    assert opt.optimize(text, mode="compress") == opt.compress(text)


def test_optimize_summary_mode():
    opt = TokenOptimizer()
    text = "Um. Dois. Tres. Quatro."
    assert opt.optimize(text, mode="summary") == opt.summarize(text)