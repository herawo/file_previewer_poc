<div>

Preview\_generator's Documentation
==================================

------------------------------------------------------------------------

Presentation
------------

This module is meant to be used inside applications to generate the
preview of a document. The context of creation of this module (as an
example of use context) was for Tracim, a github project
(https://github.com/Tracim/tracim) where users can put file on a
repository in order to share it with other users. The only way to find a
file was with his name. Hence it was decided to generate previews of the
files in order to ease the location of one.

### Format handled

### 

Verticaly : Inputs Horizontaly : Outputs

  ----------------------------------------------------------------------------
                         JPG(256²)   JPEG(1024²)    PDF   TEXT   HTML   JSON\
  ---------------------- ----------- ------------- ----- ------ ------ -------
  PNG                        OK            OK

  JPEG                       OK            OK

  BMP                        OK            OK

  GIF                        OK            OK

  PDF                        OK            OK

  Compressed\                                               OK    OK
  files\                                                               

  Office files\              OK            OK        OK
  (word, LibreOffice)\                                      OK

  Text\                                                                

                                                                       
  ----------------------------------------------------------------------------

------------------------------------------------------------------------

Installation
------------

Not written yet

------------------------------------------------------------------------

Utilisation
-----------

Here is the way it is meant to be used

from preview\_generator.model.factory import PreviewBuilderFactory
factory = PreviewBuilderFactory() mimetype =
factory.get\_document\_mimetype(document\_id) builder =
factory.get\_preview\_builder(mimetype) return
builder.get\_large\_preview(document\_id, page\_id)

Will create a preview of type Large (1024\*1024 jpeg) in a cache file

</div>
