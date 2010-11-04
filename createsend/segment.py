import json
from createsend import CreateSendBase
from utils import json_to_py

class Segment(CreateSendBase):

  def __init__(self, segment_id=None):
    self.segment_id = segment_id
    super(Segment, self).__init__()

  def subscribers(self, date, page=1, page_size=1000, order_field="email", order_direction="asc"):
    params = {
      "date": date,
      "page": page,
      "pagesize": page_size,
      "orderfield": order_field,
      "orderdirection": order_direction }
    response = self._get(self.uri_for("active"), params=params)
    return json_to_py(response)

  def delete(self):
    response = self._delete("/segments/%s.json" % self.segment_id)

  def uri_for(self, action):
    return "/segments/%s/%s.json" % (self.segment_id, action)
