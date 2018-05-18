#include <stdio.h>
#include <stdlib.h>
#include <string.h>
int main() {
    int a_rows, a_cols, t_rows, t_cols, c_rows, c_cols, row_offset;
    size_t area_len, account_len;
    char* area;
    char* account;
    int i_start, j_start, i, j;
    int blocked, tiles, curtiles;

    size_t params_size = 20;
    char* params = (char*)malloc(params_size * sizeof(char));
    ssize_t bytes_read = getline(&params, &params_size, stdin);
    while (bytes_read != -1) {
        a_rows = atoi(strtok(params, " "));
        a_cols = atoi(strtok(NULL, " "));
        t_rows = atoi(strtok(NULL, " "));
        t_cols = atoi(strtok(NULL, " "));
        c_rows = a_rows+t_rows-1;
        c_cols = a_cols+t_cols-1;
        area_len = (a_rows * a_cols + a_rows) * sizeof(char);
        area = (char*)malloc(area_len);
        fread(area, area_len, sizeof(char), stdin);
        row_offset = a_cols+1;
        account_len = c_rows * c_cols;
        account = (char*)calloc(account_len, sizeof(char));
        for (i=0; i<a_rows; i++) {
            blocked = t_cols;
            for (j=0; j<a_cols; j++) {
                if (*(area+i*row_offset+j) == 'X') {
                    blocked = 0;
                }
                else {
                    blocked += 1;
                }
                if (blocked >= t_cols) {
                    *(account+i*c_cols+j) = 'R';
                }
            }
            for (; j<c_cols; j++) {
                blocked += 1;
                if (blocked >= t_cols) {
                    *(account+i*c_cols+j) = 'R';
                }
            }
        }
        for(; i<c_rows; i++) {
            for (j=0; j<c_cols; j++) {
                *(account+i*c_cols+j) = 'R';
            }
        }
        for (j = 0; j < c_cols; j++) {
            blocked = t_rows;
            for (i = 0; i < c_rows; i++) {
                if (*(account+i*c_cols+j) != 'R') {
                    blocked = 0;
                }
                else {
                    blocked += 1;
                }
                if (blocked >= t_rows) {
                    *(account+i*c_cols+j) = 'S';
                }
            }
        }
        tiles = a_rows*a_cols;
        for (i_start = 0; i_start < t_rows; i_start++) {
            for (j_start = 0; j_start < t_cols; j_start++) {
                curtiles = 0;
                for (i = i_start; i < c_rows; i += t_rows) {
                    for (j = j_start; j < c_cols; j += t_cols) {
                        if (*(account+i*c_cols+j) != 'S') {
                            curtiles += 1;
                        }
                    }
                }
                if (curtiles < tiles) {
                    tiles = curtiles;
                }
            }
        }
        printf("%i\n", tiles);
        free(account);
        free(area);
        bytes_read = getline(&params, &params_size, stdin);
    }
}
