import unittest

from engine.splitter import split_text


class TestSplitText(unittest.TestCase):

    def test_empty_text_returns_empty_list(self):
        self.assertEqual(split_text(""), [])
        self.assertEqual(split_text("   "), [])

    def test_short_text_stays_in_one_segment(self):
        text = "Esta es una frase corta."
        result = split_text(text, max_chars=100)

        self.assertEqual(result, [text])

    def test_text_is_split_into_multiple_segments(self):
        text = (
            "Esta es la primera frase. "
            "Esta es la segunda frase. "
            "Esta es la tercera frase."
        )

        result = split_text(text, max_chars=40)

        self.assertGreater(len(result), 1)

    def test_segments_do_not_exceed_max_chars(self):
        text = (
            "Primera frase para probar el sistema. "
            "Segunda frase para probar el sistema. "
            "Tercera frase para probar el sistema."
        )

        max_chars = 50
        result = split_text(text, max_chars=max_chars)

        for segment in result:
            self.assertLessEqual(len(segment), max_chars)

    def test_long_sentence_is_split_by_words(self):
        text = (
            "NarradorAI necesita dividir correctamente una oración "
            "muy larga incluso cuando no existen puntos intermedios"
        )

        max_chars = 30
        result = split_text(text, max_chars=max_chars)

        self.assertGreater(len(result), 1)

        for segment in result:
            self.assertLessEqual(len(segment), max_chars)

    def test_invalid_max_chars_raises_error(self):
        with self.assertRaises(ValueError):
            split_text("Texto de prueba", max_chars=0)


if __name__ == "__main__":
    unittest.main()