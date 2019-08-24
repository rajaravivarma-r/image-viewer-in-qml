from string import Template

image_component = Template(
    """
Image {
  source: "file://$path"
  height: 200

  sourceSize.height: height

  autoTransform: true
  fillMode: Image.PreserveAspectFit
}
"""
)

images = [
    "/Users/rajaravivarma/Github/image-viewer/sample_images/IMG_20180901_125730164.jpg",
    "/Users/rajaravivarma/Github/image-viewer/sample_images/IMG_20180901_125732706.jpg",
    "/Users/rajaravivarma/Github/image-viewer/sample_images/IMG_20180901_125746579.jpg",
    "/Users/rajaravivarma/Github/image-viewer/sample_images/IMG_20180901_125748433.jpg",
    "/Users/rajaravivarma/Github/image-viewer/sample_images/IMG_20180901_125752646.jpg",
    "/Users/rajaravivarma/Github/image-viewer/sample_images/IMG_20180901_125856681_PORTRAIT.jpg",
    "/Users/rajaravivarma/Github/image-viewer/sample_images/IMG_20180901_125910062.jpg",
    "/Users/rajaravivarma/Github/image-viewer/sample_images/IMG_20180901_125945650.jpg",
    "/Users/rajaravivarma/Github/image-viewer/sample_images/IMG_20180901_125954483.jpg",
    "/Users/rajaravivarma/Github/image-viewer/sample_images/IMG_20180901_130026460_PORTRAIT.jpg",
    "/Users/rajaravivarma/Github/image-viewer/sample_images/IMG_20180901_130031395_PORTRAIT.jpg",
    "/Users/rajaravivarma/Github/image-viewer/sample_images/IMG_20180902_190015430.jpg",
    "/Users/rajaravivarma/Github/image-viewer/sample_images/IMG_20180902_190110905.jpg",
]

for image in images:
    print(image_component.substitute(path=image))
