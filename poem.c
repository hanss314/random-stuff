#include <stdio.h>

int main(){
    const char *poem = "Roses are red,\nThis program might halt.\nI forgot a null terminator";
    for (int i = 0; i >= 0; i++){
        printf("%c", poem[i]);
    }
    return 0;
}