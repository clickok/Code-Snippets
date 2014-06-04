# Outcome of process

We take a series of images that contain an unusually bright spots (from LEDs, say),
find the LEDs in each image, and produce a composite image that contains only the
background with the LEDs layered overtop.

For example, a robot with LEDs on top would trace out its position across time,
without including the background or blurry images of the robot as it moves around.

# Get the images

We acquire a series of JPEG images (from, say, an MJPEG video) and convert them
to PNG files. Assuming the images are in the current directory, we use:

`$ mogrify -format png *.jpg`

# Isolate the bright spots

We use thresholding above a certain level to identify the LEDs.

We can convert all pixels below a threshold (here for the Red and Green channels)
to black via:

`$ convert INPUT.png -channel Red,Green -black-threshold 50% OUTPUT.PNG`

# Making non-bright spots transparent

We make the non-bright spots (which are now black thanks to the last command)
transparent via:

`$ convert INPUT.png -fuzz 5% -transparent black OUTPUT.png`

The `-fuzz 5%` part was not needed here because the non-bright pixels are pure
black.

# Combine images together

*	In sequence (perhaps with a color gradient to show trajectory?)

To convert all NON-transparent pixels to some color (here red):

`$ convert INPUT.png -channel rgba -fill red +opaque none OUTPUT.png`

Or, if we specify the fill color more precisely, noting that (0,0,0,0) is opaque black:

`$ convert test6.png -channel rgba -fill "rgba(255,0,0,0)" +opaque none OUTPUT.png`


For an entire directory:

`$ mogrify -path OUTPUT_DIR/ -channel rgba -fill red +opaque none INPUT_DIR/*.png`


*	Combine isolated bright spots together, then onto a background image

First we combine the (transparent?) images via:

`$ convert INPUT_DIR/*.png -background none -layers flatten OUTPUT.png`

Then we merge them with the actual background image:

`$ convert COMBINED_IMG.png BACKGROUND.png -background none -layers flatten OUTPUT.png`


# Make a movie

*	Perhaps with pairs made w/ background?