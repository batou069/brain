# A Layman introduction to Kernel Approximations

Now, more than ever, machine learning problems are set out to deal with problems in scales never witnessed before. With a growing influx of data, models are supposed to make predictions based on the knowledge extracted from millions of data observed in split seconds. In this scenario, kernel methods are one of the main tools in the machine learning toolbox, but it lags behind others due to its inefficiency on dealing with large data. Recent research has provided a new edge to the said method using the so-called “kernel-approximation” methods.

To understand this, we should first understand the general repertoire of machine learning, more specifically, linear separation methods. Assume we have a dataset consisting of several data points which we’d like to classify into categories. Each data point contains useful information which clues about what category they may belong to. Our model extracts this information and draws a decision surface to separate these data points into different categories. We fine-tune this model through a set of parameters to better fit the dataset. There is but one drawback to this method, we’ve assumed the dataset are linear separable which is rarely the case.

Linear classifiers are well cherished owing to their simplicity and yet, it’s the same simplicity which proves to be its doom. We can’t expect a naive linear classifier to properly grasp the nuances of the dataset. To get around this, we utilize what’s called feature mapping. Essentially, they make our data linearly separable by projecting these data points to a higher-dimensional space(Fig. 1). By doing so, the subtle details become much more apparent to our model. While there are a plethora of options to choose from, kernel methods outshine them all.

![](https://miro.medium.com/v2/resize:fit:579/1*S4wo_EDAX88l0M_H2IHHhg.jpeg)

Fig.1: Non-linear dataset(upper-left) projected on higher dimensional space(upper-right) making it linearly separable(lower-left). Projecting it back to original space gives us curved decision line(lower-right). [^1]
Ideally, we would want to be extravagant in this process of feature mapping, the more the merrier. Of course, that’s not the case, as it comes at the cost of increased computational complexity. To combat this curse of dimensionality, we employ the “kernel trick”. The “trick” factor is that it shifts the computational dependency from the number of dimensions to number of data points(Hofmann). What this means is we could possibly project it “in a theoretical feature space of infinite height”(Hofmann). However, this too has its setbacks, more clearly “One limitation of kernel methods is their high computational cost, which is at least quadratic in the number of training examples”(Yang et al.). In the modern era, it is only reasonable to expect millions of data points, hence calculation in its quadratic terms is wishful thinking at best.

The kernel trick method was prevalent during the infancy of machine learning, i.e. before the data boom. One can’t help but imagine, what if we could have the best of both worlds? What if we could use the simplicity of linear models but still utilize the power of kernel methods? Kernel approximation is the answer to our prayers. Before we dive deep, let’s first understand some basic sampling theory. When we randomly sample from a distribution, we get a rough idea of what the actual distribution looks like, hence the more we sample the better our approximation. This is the reason why “randomly transform their inputs have been resurfacing in the machine learning community” (Rahimi et al.). This is the foundation of Random Fourier Features loosely speaking.

Zoom image will be displayed

![](https://miro.medium.com/v2/resize:fit:700/1*aMf1dwhOG8nGfB4ZdFW5Hw.png)

Fig. 2: Difference between linear and non-linear classifiers in the specific case of SVM. This picture eloquently sums up the entire dilemma of kernel methods. [^2]

Random Fourier Features combines the power of both linear and non-linear machine. That is to say, it has the grasping capability of the non-linear machine and the simplicity of linear machines. It does so by randomly sampling the kernel and use the linear methods to get approximate of answer(Rahimi et al.). With this, we have knob using which we can control the complexity of our model. This provides two-fold advantages, it makes the algorithm both faster than the kernel trick (since we’re using linear machine) and also makes the fitting procedure simpler(Rahimi et al.)

As a final note, Random Fourier Features is just one of many kernel approximation methods. There is a whole new world exploring all these approximation techniques and we’ve just scratched the surface. With that said, kernel approximations just might be the answer for faster and scalable machine learning algorithms, but only time will tell if that’s truly the case.

[^1]: Src: [Shini Renjith,](https://www.researchgate.net/profile/Shini_Renjith) [https://www.researchgate.net](https://www.researchgate.net)
[^2]: Src: [Andrea Vedaldi](http://www.vlfeat.org/~vedaldi).