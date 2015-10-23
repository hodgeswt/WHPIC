(*
 *
 * Grammar by Will Hodges on 10/23/15
 *
 *)
start =
	{expr}
	;

expr = 
	{INT} OP {INT} ';' 
	;
	
INT = 
	{digit}
	;
	
digit =
	"0" | "1" | "2" | "3" | "4" | "5" | "6" | "7" | "8" | "9"
	;

OP = 
	"+" | "-" | "*" | "/"
	;