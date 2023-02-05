import random
from matplotlib import pyplot as plt, animation


def quick_sort(sequence):
    length = len(sequence)
    if length <= 1:
        return sequence
    else:
        pivot = sequence.pop()

    items_greater = []
    items_lower = []

    for item in sequence:
        if item > pivot:
            items_greater.append(item)

        else:
            items_lower.append(item)

    yield quick_sort(items_lower) + [pivot] + quick_sort(items_greater)


def visualize():
	
	N = random.sample(range(1, 101), 100)
	A = list(N)
	random.shuffle(A)
	
	# creates a generator object containing all
	# the states of the array while performing
	# sorting algorithm
	generator = quick_sort(A)
	
	# creates a figure and subsequent subplots
	fig, ax = plt.subplots()
	ax.set_title("Bubble Sort O(n\N{SUPERSCRIPT TWO})")
	bar_sub = ax.bar(range(len(A)), A, align="edge")
	
	# sets the maximum limit for the x-axis
	ax.set_xlim(0, 100)
	text = ax.text(0.02, 0.95, "", transform=ax.transAxes)
	iteration = [0]
	
	# helper function to update each frame in plot
	def update(A, rects, iteration):
		for rect, val in zip(rects, A):
			rect.set_height(val)
		iteration[0] += 1
		text.set_text(f"# of operations: {iteration[0]}")

	# creating animation object for rendering the iteration
	anim = animation.FuncAnimation(
		fig,
		func=update,
		fargs=(bar_sub, iteration),
		frames=generator,
		repeat=True,
		blit=False,
		interval=15,
		save_count=90000,
	)
	
	# for showing the animation on screen
	plt.show()
	plt.close()


if __name__ == "__main__":
	visualize()