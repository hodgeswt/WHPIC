(*
 *
 * Grammar by Will Hodges on 10/23/15
 *
 *)
start = (* Create our starting node *)
	{expr} (* one or more expressions *)
	; (* end node *)

expr = (* Create our expression item *)
	{INT} OP {INT} ';' (* one or more integers, an operator, and one or more integers *)
	; (* End *)
	
INT = (* Create our integer item *)
	{digit} (* one or more digits *)
	; (* End *)
	
digit = (* Create our digit item *)
	"0" | "1" | "2" | "3" | "4" | "5" | "6" | "7" | "8" | "9" (* Any one of 0-9 *)
	; (* End *)

OP = (* Create our operator item *)
	"+" | "-" | "*" | "/" (* Any +-*/ *)
	; (* End *)