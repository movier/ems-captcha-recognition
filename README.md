In this repository our task is to recognize captcha from EMS using AI. 
A sample captcha looks like this:

![EMS captcha sample](ems_captcha_sample.jpg)

To learn more about the background please read my blog [post](http://movier.me/blog/2018/train-my-first-machine-learning-model/).

It's a pipenv project. Install pipenv and libraries and run following commands to start Jupyter Notebook.

```bash
pipenv shell
jupyter notebook
```

To generate training data:
```sh
python captcha.py
```

To retrain a model:
```sh
python -m scripts.retrain \
  --bottleneck_dir=tf_files/bottlenecks \
  --how_many_training_steps=500 \
  --model_dir=tf_files/models/ \
  --summaries_dir=tf_files/training_summaries/mobilenet_0.50_128 \
  --output_graph=tf_files/retrained_graph.pb \
  --output_labels=tf_files/retrained_labels.txt \
  --architecture=mobilenet_0.50_128 \
  --image_dir=digit_images
```

To predict a captcha:
```sh
python -m scripts.label_image --image=ems_captcha_sample.jpg
```