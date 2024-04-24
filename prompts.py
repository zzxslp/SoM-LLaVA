'''
prompts for calling GPT-4V.

instrucions are appended to the dataset (random sampling an instruction from the pool as question),
no need to feed instruction into GPT-4V
'''


instruction_pool = [
    "I have labeled a bright numeric ID at the center for each visual object in the image. Please enumerate their names.",
    "Each item in the image has been marked with a distinct numeric identifier at its center. Please list the names of these items in order of their tags.",
    "For every visual object in the photo, a unique numeric ID has been placed centrally. Could you enumerate these objects by their assigned numbers?",
    "In the picture, every object is tagged with a central numeric ID. I'd like you to identify and list each object based on its numeric tag.",
    "A numeric ID has been centrally labeled on each object within the image. Can you list all the objects, referencing them by their numeric IDs?",
    "Every object visible in this image carries a numeric ID at its core. Please catalog the objects by their corresponding numbers.",
    "This image features various objects, each highlighted by a numeric ID in the center. Could you itemize the objects using these numeric identifiers?",
    "Identify each object in the image, noting that a numeric ID centrally labels each one. Please list the objects as per their numeric tags.",
    "I've assigned a numeric ID to the center of each object in this image. Can you list the objects, mentioning them by their numeric IDs?",
    "In this image, every object has been given a numeric ID at its midpoint. Could you provide a list of these objects, ordered by their numeric IDs?",
    "A bright numeric ID has been centrally placed on each object within the image. Please enumerate the objects, referring to them by these IDs.",
    "This image features numeric tags positioned above various objects, both items and parts of the background. Please provide a list of what these tags represent.",
    "In the provided image, you'll find numeric tags placed over certain objects and background elements. Could you identify and list these tagged entities?",
    "Numeric tags can be seen on top of some objects and background areas in this image. List out the names of the tagged items and elements.",
    "Several objects and background details in the image have been marked with numeric tags. Can you list each by name?",
    "Look at this image where numeric tags hover over different objects, including items and the background. Identify and record the names of these tagged things.",
    "The image shows various objects and parts of the background adorned with numeric tags. Please enumerate the objects and areas these tags correspond to.",
    "Notice the numeric tags on certain items and background portions in the image? List the names of these tagged objects and areas.",
    "This image includes numeric tags on top of some objects and background features. Catalog the names of the entities marked by these tags.",
    "In this image, numeric tags have been assigned to select items and background elements. Could you list the names associated with each tag?",
    "Some objects and background details in the provided image carry numeric tags. Please list the names of these numerically tagged items and features.",
    "Observe the numeric identifiers placed on objects within the image. Detail the names associated with these numbers.",
    "With numeric IDs marking certain features and objects in this image, could you outline what each number refers to?",
    "This picture displays items and background features with numeric labels. Who can catalog the entities these numbers denote?",
    "Given the image with items and areas marked by numeric tags, please identify and enumerate these marked subjects.",
    "In this image, you'll notice items and background aspects labeled with numbers. What do these numeric labels signify? Please list them.",
    "Numeric labels have been affixed to a variety of objects in the enclosed image. Can you decipher and list what these labels identify?",
    "Please review the image where numeric IDs are visible on certain items and areas. List the names that correspond to each ID.",
    "Spot the numeric tags in the image? They mark various items and parts of the scene. List out what each tag represents.",
    "This image is annotated with numeric IDs on specific objects and background elements. Could you provide a rundown of these tagged locations and items?",
    "Look at the numeric tags scattered across items and the background in this image. Can you compile a list of these items as they are tagged?",
    "Each numeric ID in the image relates to an object or an area. Please identify and make a list based on these IDs.",
    "You'll find objects and background features tagged with numbers in the image provided. Enumerate the tagged items, please.",
    "With several objects and sections tagged numerically in this image, can you list and identify what's behind each number?",
    "This image includes numeric tags over certain features and items. Detail what lies beneath each numeric indicator.",
    "Notice the numeric IDs on various elements within this image? Please list what each number is tagging.",
    "Certain objects and background segments in this image are earmarked with numeric IDs. Can you list these identified by their numbers?",
    "The image showcases various items and parts of the background marked with numeric IDs. What do these numbers reveal? Please list.",
    "In this image, items and background elements bear numeric tags. Enumerate the contents as identified by these tags.",
    "Given the numeric tags you see on this image's items and background, can you delineate what each tag is marking?",
    "This picture is marked with numeric IDs highlighting different objects and areas. Please list the identifications associated with these numbers.",
    "Here is an image with numeric tags on top of some objects (items or background). List the names of these things."
]

img_ex1 = load_image(f"./data/coco/som_train2017/000000000025.jpg")
img_ex2 = load_image(f"./data/coco/som_train2017/000000000036.jpg")
img_raw = load_image(f"./data/coco/som_train2017/{iput_img_id}.jpg")

body = [{ 'role': 'system',
           'content': ['''You are an AI visual assistant. 
           You will be presented with an image with numeric ID tags at the centers of some objects. 
           Note the tags are on top of (at the center of) each object, you should not assign a tag to an object away from it.
           Try you best to list all tagged items one by one, if there is occlusion or you are not sure what is the item behind a particular tag, you can explicitly say it out.
'''],},
{ 'role': 'user', 'content': [{"image": img_ex1}],},
{ 'role': 'assistant',
  'content': ['''
  Here are the items tagged in the image:
  1. The branch of a tree that is lying on the ground.
  2. The lower body of a giraffe, which is mostly occluded by the rising ground in front of it.
  3. The tag is placed on a tree, there are legs of a giraffe next to it.
  4. The same tree on the ground from tag-1, tag 4 is close to the tail of a giraffe with tag-8.
  5. Green Grass.
  6. The blue Sky, possibly with cloud.
  7. The leaves of a different, possibly smaller tree or bush.
  8. The body of a giraffe that is standing up.
  9. Bush in the background, on top of the giraffe lying down and tagged with id 2.
  10. This tag is placed over a tree, which is in the background and not fully clear due to the distance and foliage.
  Please note that tags are not always placed exactly at the center of each object, but they provide a general location of the object they correspond to.
  ''']},

{ 'role': 'user', 'content': [{"image": img_ex2}],},
{ 'role': 'assistant',
  'content': ['''
1. Blue water (possibly a lake or river)
2. The tag is placed on top of a woman's left hand, with a portion of blue water in the background.
3. A green forest from a distance, on the other side of the water.
4. It is not clear which object this tag points to, possibly the tree in the background or the white chair.
5. A white wooden structure, possibly a lifeguard chair.
6. Sky, with a small portion of a sign on top of this tag.
7. Sky with Clouds.
8. A swimsuit or a person's torso wearing a swimsuit.
9. A pink umbrella.
The image does not provide enough detail to conclusively identify some of the tagged items, particularly tags numbered 2, 4, and 6.
''']},

{ 'role': 'user', 'content' : [{"image": img_raw}],},
]

