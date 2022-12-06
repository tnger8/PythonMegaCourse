contents = ["all foxes jump the fence", "The carrots are delicious", "I love to eat cakes"]

filenames = ["file1.txt", "Reports.txt", "Presentation.txt"]

for content, filename in zip(contents, filenames):
    file = open(f"{filename}", 'w')
    file.write(content)