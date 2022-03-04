#include<stdio.h>
void main()
{ int edad=0;
  char nombre[9];
  printf("\nCuantos anios tienes: ");
  scanf("%d",&edad);
  printf("\nCual es tu nombre: ");
  scanf("%s",&nombre);
  printf("\n Tengo %d anios y me llamo %s ",edad, nombre);
}