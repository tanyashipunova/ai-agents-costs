# Cost calculation for a scenario with bugs
# A project base context = 50 000 tokens

# Point 2 on the sequence diagram
in_1 = 50000
out_1 = 2000

# Point 3
in_2 = in_1 + out_1 # 52000
out_2 = 2000

# Point 4
in_3 = in_2 + out_2 # 54000
out_3 = 1500

# Point 5
in_4 = in_3 + out_3 # 55500
out_4 = 2000

# Point 6
in_5 = in_4 + out_4 # 57500
out_5 = 1500

# Point 7
in_6 = in_5 + out_5 # 59000
out_6 = 1000

# Point 8
in_7 = in_6 + out_6 # 60000
out_7 = 2000

# Point 9
in_8 = in_7 + out_7 # 62000
out_8 = 1500

# Point 10
in_9 = in_8 + out_8 # 63500
out_9 = 500

# Point 11
in_10 = in_9 + out_9 # 64000
out_10 = 2000

total_in = in_1 + in_2 + in_3 + in_4 + in_5 + in_6 + in_7 + in_8 + in_9 + in_10
total_out = out_1 + out_2 + out_3 + out_4 + out_5 + out_6 + out_7 + out_8 + out_9 + out_10

print(f"in_1: {in_1}, out_1: {out_1}")
print(f"in_2: {in_2}, out_2: {out_2}")
print(f"in_3: {in_3}, out_3: {out_3}")
print(f"in_4: {in_4}, out_4: {out_4}")
print(f"in_5: {in_5}, out_5: {out_5}")
print(f"in_6: {in_6}, out_6: {out_6}")
print(f"in_7: {in_7}, out_7: {out_7}")
print(f"in_8: {in_8}, out_8: {out_8}")
print(f"in_9: {in_9}, out_9: {out_9}")
print(f"in_10: {in_10}, out_10: {out_10}")

print(f"Total Ins: {total_in}")
print(f"Total Outs: {total_out}")
