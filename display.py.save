#!/usr/bin/python

def display(data):
	readings = []
	if (len(data) == 5):
		readings.append((data[0],data[1],data[2],data[3],data[4]))
		


	for reading in readings:
		print '\t'.join(str(i) for i in reading)
		print("-------------------------------------")






# def format_matrix(header, matrix,
#                   top_format, left_format, cell_format, row_delim, col_delim):
#     table = [[''] + header] + [[name] + row for name, row in zip(header, matrix)]
#     table_format = [['{:^{}}'] + len(header) * [top_format]] \
#                  + len(matrix) * [[left_format] + len(header) * [cell_format]]
#     col_widths = [max(
#                       len(format.format(cell, 0))
#                       for format, cell in zip(col_format, col))
#                   for col_format, col in zip(zip(*table_format), zip(*table))]
#     return row_delim.join(
#                col_delim.join(
#                    format.format(cell, width)
#                    for format, cell, width in zip(row_format, row, col_widths))
#                for row_format, row in zip(table_format, table))
