alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print("Original x-position: " + str(alien_0['x_position']))
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
	x_increment = 3
#print((alien_0["x_position"] + x_increment))
alien_0["x_position"] = alien_0["x_position"] + x_increment
print("New x-position: " + str(alien_0['x_position']))




favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'ruby',
'phil': 'python',
}
print("Sarah's favorite language is "
 +  favorite_languages['sarah'].title()
 +
 ".")