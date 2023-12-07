# import matplotlib

# Get the radius from the user
r = float(input("Enter the radius: "))
pi = 3.14
circumference = 2 * pi * r
area = pi * (r ** 2)

# Draw the graph of the circle
circle = plt.Circle((0, 0), r, edgecolor='purple', facecolor='gray')
fig, ax = plt.subplots()
ax.add_patch(circle)
ax.set_aspect('equal', adjustable='datalim')

# Set graph properties
plt.xlim(-r - 1, r + 1)
plt.ylim(-r - 1, r + 1)
plt.axhline(y=0, color='red')
plt.axvline(x=0, color='black')
plt.title('Circle')
plt.xlabel('X Axis')
plt.ylabel('Y Axis')

# Show the graph
plt.show()

print(f"Area: {area}, Circumference: {circumference}")




# # daire alan

pi = 3.14159
radius = int(input("Enter radius... "))
circle_area = radius*radius
circle_circumference = 2 * pi * radius

print("1)Radius = ",radius, "\n2)Circle area = ", circle_area)
print("\n------------------------------------\nThank you for using my program :) <3")
