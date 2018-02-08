FILE_NAME = 'text.txt'


def check_page(file, n_lines, max_char, max_lines, pages=0):
	if n_lines == (max_lines-1):
		pages += 1
		n_lines = 0
		file.write('{0} - Page[{1}]\n'.format(FILE_NAME.rjust(int(max_char/2), ' '), pages))
	return pages, n_lines
	

def format_pages(file, max_char, max_lines):

	new_page = open('Pages.txt', 'w', encoding='utf-8')
	pages, n_lines = 0, 0
	
	for line in file.readlines():
		words = line.split(' ')
		new_line = ''
		
		for w in words:
			w = w.strip()
			
			if (len(new_line) + len(w)) + 1 > max_char:
				new_page.write(new_line+'\n')
				n_lines += 1
				new_line = ''
				pages, n_lines = check_page(new_page, n_lines, max_char, max_lines, pages)

			new_line += w + ' '
			
		if new_line != '':
			n_lines += 1
			new_page.write(new_line+'\n')
			pages, n_lines = check_page(new_page, n_lines, max_char, max_lines, pages)
					 
					
def main():
	FILE = open(FILE_NAME, encoding='utf-8')
	format_pages(FILE, 76, 60)
	FILE.close()
	
main()