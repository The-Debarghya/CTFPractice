'''
asm3:
	<+0>:	push   ebp
	<+1>:	mov    ebp,esp
	<+3>:	xor    eax,eax
	<+5>:	mov    ah,BYTE PTR [ebp+0x9]
	<+8>:	shl    ax,0x10
	<+12>:	sub    al,BYTE PTR [ebp+0xe]
	<+15>:	add    ah,BYTE PTR [ebp+0xf]
	<+18>:	xor    ax,WORD PTR [ebp+0x12]
	<+22>:	nop
	<+23>:	pop    ebp
	<+24>:	ret    
'''
def asm3(param_1, param_2, param_3):
    return ((param_2 >> 24) << 8 | (-(param_2 >> 16) & 0xFF)) ^ (param_3 >> 16)

def main():
    # Test input values
    param1 = 0xd2c26416
    param2 = 0xe6cf51f0
    param3 = 0xe54409d5

    # Call asm3 function with the test inputs
    result = asm3(param1, param2, param3)

    # Print the result
    print(f"The result of asm3 function is: 0x{result:04x}")

if __name__ == "__main__":
    main()
