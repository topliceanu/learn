# Backend for instagram photos

1. Problem exploration
- What are the feature I'm looking to support?
    Upload, view feed, comment on a picture, follow other users.
- Are photos stored in raw format? Is it ok if we archive them?
- What's the life of an uploaded photo look like?
  - How many times is it used in the first day after upload? First week? First month? After that?
- Numbers:
  - how many photos uploaded a day? Any spikes that the system needs to support? 2M 23photos/second
  - how many users does the platform have? How many active users
  - how many photo impressions does the platform have?
  - how many photos/accounts are popular (relevant for the cache)? 100M
  - what is the average size of an uploaded photo? 200KB
- What other type of data can be attached to a photo? coordinates, comments, reactions, etc.
- How is the feed of photos calculated?

2. High level overview
- service is read-heavy. The read and write paths should be different.
- separate storage of image bytes from storage of metadata about images.
- sharding of storage
- focus is on availability, not consistency, an image that is not available to everyone immediately after upload is fine!
- caching of recent images

3. Solution breakdown
- read path: client queries the FE with an image id, the FE gets the location for that image from metadata server, then tells redirects the client to that image.
- write path: client signals to the FE that it wants to upload a photo. The FE asks the Metadata server where to upload it, the FE gets that info back to the client, the client uploads the photo to the Storage server, the Storage server updates the metadata server.
- storage server is sharded: the MS' job is to find a location for the photo. You want an even load on storage boxes. You want to be able to add capacity, you want to reshuffle popular images.
- hot images/accounts: add a layer of caching for images so we don't go to the storage servers.
- reshuffling, we want to move popular images to less used boxes!
- blob storage does image compression, stores images in different formats, say for mobile phones.

Data modelling:
- User: id, name, email, ..
- Photo: id, title, caption, lat, long, created_at, tags
