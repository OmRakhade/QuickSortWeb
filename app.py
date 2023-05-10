from flask import Flask, render_template, request
import random

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def result():
    unsorted_list = request.form.get('unsorted_list')
    unsorted_list = [int(i) for i in unsorted_list.split()]
    sorted_list = quick_sort(unsorted_list)
    return render_template('result.html', sorted_list=sorted_list)

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = random.choice(arr)
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

if __name__ == '__main__':
    app.run(debug=True)