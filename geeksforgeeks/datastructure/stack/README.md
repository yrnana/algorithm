https://www.geeksforgeeks.org/stack-data-structure/

| infix             | prefix        | postfix       |
| ----------------- | ------------- | ------------- |
| A + B * C + D     | + + A * B C D | A B C * + D + |
| (A + B) * (C + D) | * + A B + C D | A B + C D + * |
| A * B + C * D     | + * A B * C D | A B * C D * + |
| A + B + C + D     | + + + A B C D | A B + C + D + |