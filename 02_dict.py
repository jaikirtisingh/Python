marks={
    "jai":100,
    "raju":30,
    "ram ":23
}
print(marks.item())
print(marks.keys())
print(marks.value())
marks.update({"jai":99})
print(marks)
print(marks.get("jai"))#print none
print(marks["jai"])#return error