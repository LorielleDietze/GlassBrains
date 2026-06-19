# How to make a glass brain for neuroimaging visualizations

## Protocol:

1.	Have specific white matter tracts that you want to add in a glass brain.

2.	Obtain the smd, other effect sizes, or p-values for each tract to see a gradient in the final brain.

3.	Set directory in terminal (ls and cd commands) Make a folder specifically for masks to go into and set the directory there.

4.	In FSLeyes save the full JHU ICBM-DTI-81 WM atlas for all the coordinates.

5.	Separate each tract in FSLeyes using the JHU ICBM-DTI-81 WM atlas to find the L and R coordinates. You open the atlas and click on the ROI. This ROI has a number that you use for the thresholds in terminal. 

6.	Bilateral tracts can be combined by selecting the coordinates for both in fsleyes or using terminal, this works for unilateral tracts as well. (-thr and -uthr commands)

7.	Binarize the individual masks by making the surrounding areas 0s and the specific tract 1s. (-bin command)

8.	Multiply the mask by the smd. (-mul command)

9.	Combine the multiple tract masks to the larger brain mask that need to be the same colour scale. (-add command)

10.	Add code to MRICroGL for the glass brain template, change transparency/colour based on preference.

11.	Add each overlay of the nii mask to the glass brain and change the colour of the overlay to the appropriate colour scale.

12.	Save as bitmap for the highest resolution in each orientation, do not screenshot.

13.	Advanced: You can make a spinning brain gif from MRIcroGL by modifying the code to include k-steps and k-time between each image. This can be exported as well.


## FSLeyes Code: 
### In terminal

Step 3: Use ls to see what is in your current directory, cd to change the directory.

Step 6: fslmaths JHU-labels_label_all.nii.gz -thr [lower coordinate] -uthr [upper coordinate] JHU_[tractname].nii.gz

Step 7: fslmaths JHU_[tractname].nii.gz -bin JHU_[tractname]_bin.nii.gz

Step 8: fslmaths JHU_[tractname]_bin.nii.gz -mul [effect size or p-value] JHU_[tractname]_[what it means bmi or dx].nii.gz

Step 9: fslmaths JHU_[tractname]_bmi.nii.gz -add JHU_[tractname]_bmi.nii.gz -add JHU_[tractname]_bmi.nii.gz -add JHU_[tractname]_bmi.nii.gz JHU_bmi_mask.nii.gz


## Glass Brain Code:
### In MRIcroGL scripting

See MRIcroGL_Glass_Brain.py