#!/usr/local/bin/python

if __name__ == "__main__":
	f_in = open("input.txt", "r")
	f_out = open("input_trimmed.txt", "w")
	for line in f_in:
		trimmed = line[14:]
		f_out.write(line)
		print(f"length: {len(trimmed.rstrip())}")
	f_out.close()
	f_in.close()
