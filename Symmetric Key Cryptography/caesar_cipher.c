#include<stdio.h>
#include<ctype.h>

void CaesarCipher(char text[], int shift){
    for(int i=0; text[i] != '\0'; i++){
        char ch = text[i];

        if (isalpha(ch)){
            char shiftbase = isupper(ch) ? 'A' : 'a';
            text[i] = (ch - shiftbase + shift) % 26 + shiftbase;
        }
    }
}

void DecryptCaesarCipher(char text[], int shift){
    CaesarCipher(text, -shift);
}

int main(){
    char text[] = "HELLO WORLD";
    int shift = 3;

    CaesarCipher(text, shift); 
    printf("Encrypted Text: %s\n", text);

    DecryptCaesarCipher(text, shift);
    printf("Decrypted Text: %s\n", text);
}