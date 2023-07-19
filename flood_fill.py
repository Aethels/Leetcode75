def flood_fill(image, sr, sc, color):
    # get the original value of the pixel at (sr, sc)
    old_value = image[sr][sc]
    # if the old value is the same as the new color, return the image
    if old_value == color:
        return image
    # get the number of rows and columns in the image
    m = len(image)
    n = len(image[0])
    # define a helper function to fill the adjacent pixels
    def fill(r, c):
        # check if the pixel is within the image boundaries
        if r < 0 or r >= m or c < 0 or c >= n:
            return
        # check if the pixel has the same value as the old value
        if image[r][c] == old_value:
            # change the pixel value to the new color
            image[r][c] = color
            # fill the four adjacent pixels recursively
            fill(r-1, c) # up
            fill(r+1, c) # down
            fill(r, c-1) # left
            fill(r, c+1) # right
    # call the helper function on the starting pixel
    fill(sr, sc)
    # return the modified image
    return image


image = eval(input("Enter your image: "))
sr, sc, color = map(int, input("Enter your sr, sc, and color: ").split())

print(flood_fill(image, sr, sc, color))
