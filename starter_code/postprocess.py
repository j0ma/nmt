import sys
import os


def count_parens(lt):
    n_open = 0
    n_close = 0
    for c in lt:
        if c == '(':
            n_open += 1
        elif c == ')':
            n_close += 1
    return n_open, n_close

def balanced(lt):
    n_open, n_closed = count_parens(lt)
    return n_open == n_closed

def clean_rows(rows):
    output = []
    for row in rows:
        n_open, n_close = count_parens(row)
        if n_open < n_close:
            n_rm = n_close - n_open
            print(f'about to remove {n_rm} closing parens')
            # remove extraneous closing parens from end
            clean_row = []
            for char in reversed(row):
                if char == ')' and n_rm > 0:
                    n_rm -= 1
                    continue
                else:
                    clean_row.append(char)
            clean_row = "".join(reversed(clean_row))
        elif n_close < n_open:
            n_add = n_open - n_close
            clean_row = row + n_add*' )'
        else:
            clean_row = row

        if not balanced(clean_row):
            print('Imbalanced row!')
            no, nc = count_parens(clean_row)
            print(no, nc)
            print(clean_row)

        output.append(clean_row)

    return output

if __name__ == '__main__':
    input_folder, output_folder = sys.argv[1], sys.argv[2]
    # find all files in input folder
    input_files = os.listdir(input_folder)
    for fn in input_files:
        with open(f"{input_folder}/{fn}", 'r') as f:
            input_file_rows = f.read().split('\n')
            output_rows = clean_rows(input_file_rows)

        with open(f"{output_folder}/{fn}.postprocessed", 'w') as f_out:
            f_out.write("\n".join(output_rows))



