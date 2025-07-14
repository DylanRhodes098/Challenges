from readmeGenerator import a
from richLibraryFunction import loading_simulation

loading_simulation()
print(a)

with open("README.md", "w") as f:
    f.write(f"{a}")
