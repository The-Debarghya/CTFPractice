#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#define SIZE 70
typedef struct{
  int arr[SIZE];
  int top;
} stack;
void swap(int *top1, int *top2) {
  int t = *top1;
  *top1 = *top2;
  *top2 = t;
}
bool is_empty(stack s){  //check if the stack is empty
    if(s.top == -1)
        return true;
    else
        return false;
}
bool is_full(stack s){    //check if the stack is full
    if(s.top==(SIZE-1))
        return true;
    else
        return false;
}
int push(stack *s, int n){     //push new element to stack
    if(is_full(*s)){          //check stack is full or not
        return 0;
    }
    s->top = s->top+1;
    s->arr[s->top] = n;
    return n;
}
int pop(stack *s){   //to store and print which number is deleted
    int temp;
    if(is_empty(*s))     //check for empty stack
        return 0;
    temp = s->arr[s->top];
    s->top  = s->top-1;
    return temp;
}
int main() {
  stack s1, s2, s3;
  char ch;
  int n, temp;
  s1.top = -1;
  push(&s1, 0);
  s2.top = -1;
  s3.top = -1;
  FILE *fp;
  fp = fopen("input.txt", "r");
  while ((ch=fgetc(fp)) != EOF) {
    if (ch == '+') {
      n = pop(&s1);
      n = n+1;
      push(&s1, n);
    } else if (ch == '-') {
      n = pop(&s1);
      n = n-1;
      push(&s1, n);
    } else if(ch == '@'){
      swap(&s1.arr[s1.top], &s1.arr[s1.top-1]);
    } else if(ch == '.'){
      n = pop(&s1);
      push(&s1, n);
      push(&s1, n);
    } else if(ch == '>'){
      while (s1.top != 0) {
        n = pop(&s1);
        push(&s2, n);
      }
       temp = s1.arr[s1.top];
       pop(&s1);
       while (s2.top != -1) {
         n = pop(&s2);
         push(&s1, n);
       }
       push(&s1, temp);
    }else if(ch == '<'){
      temp = pop(&s1);
      while (!is_empty(s1)) {
        n = pop(&s1);
        push(&s3, n);
      }
      push(&s1, temp);
      while (!is_empty(s3)) {
        n = pop(&s3);
        push(&s1, n);
      }
    }
  }
  fclose(fp);
  printf("CTFlearn{");
  for (int i = 0; i <= s1.top; i++) {
    printf("%c", s1.arr[i]);
  }printf("}\n");
  return 0;
}
