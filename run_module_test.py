# Here is where I run all of the packages module unit tests

set_of_test = ["image_disjoint_set.py", "image_graph.py"]

for test in set_of_test:
	execfile(test)

print("All Tests: COMPLETE")