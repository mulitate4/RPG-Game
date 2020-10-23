def border_msg(sentences: list, indent = 1):
	space = " "*indent
	max_sentence = 0
	for sentence in sentences:
		item_length = len(sentence)
		if item_length > max_sentence:
			max_sentence = item_length

	box_top_left = u"\u2554"
	box_double_line = u"\u2550"
	box_top_right = u"\u2557"
	box_vert_double_line = u"\u2551"

	box = box_top_left + (2 * indent + max_sentence)*box_double_line + box_top_right +"\n"

	for sentence in sentences:
		box += f'{box_vert_double_line}{space}{sentence}{" "*(max_sentence - len(sentence))}{space}{box_vert_double_line}\n'

	box += f'╚{"═" * (max_sentence + indent * 2)}╝'  # lower_border
	print(box)

border_msg(["ok", "whylol", "FCASIONC"])