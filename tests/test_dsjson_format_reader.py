import io
import vowpal_wabbit_next as vw


def test_single() -> None:
    text_input = """{"_label_cost":-0.0,"_label_probability":0.05000000074505806,"_label_Action":4,"_labelIndex":3,"o":[{"v":0.0,"EventId":"13118d9b4c114f8485d9dec417e3aefe","ActionTaken":false}],"Timestamp":"2021-02-04T16:31:29.2460000Z","Version":"1","EventId":"13118d9b4c114f8485d9dec417e3aefe","a":[4,2,1,3],"c":{"FromUrl":[{"timeofday":"Afternoon","weather":"Sunny","name":"Cathy"}],"_multi":[{"_tag":"Cappucino","i":{"constant":1,"id":"Cappucino"},"j":[{"type":"hot","origin":"kenya","organic":"yes","roast":"dark"}]},{"_tag":"Cold brew","i":{"constant":1,"id":"Cold brew"},"j":[{"type":"cold","origin":"brazil","organic":"yes","roast":"light"}]},{"_tag":"Iced mocha","i":{"constant":1,"id":"Iced mocha"},"j":[{"type":"cold","origin":"ethiopia","organic":"no","roast":"light"}]},{"_tag":"Latte","i":{"constant":1,"id":"Latte"},"j":[{"type":"hot","origin":"brazil","organic":"no","roast":"dark"}]}]},"p":[0.05,0.05,0.05,0.85],"VWState":{"m":"ff0744c1aa494e1ab39ba0c78d048146/550c12cbd3aa47f09fbed3387fb9c6ec"},"_original_label_cost":-0.0}"""
    workspace = vw.Workspace(["--cb_explore_adf"])
    parser = vw.DSJsonFormatParser(workspace)
    result = parser.parse_json(text_input)
    assert len(result) == 5
    assert isinstance(result, list)


def test_single_formatted() -> None:
    text_input = """{
  "_label_cost": -1.0,
  "_label_probability": 0.8500000238418579,
  "_label_Action": 1,
  "_labelIndex": 0,
  "o": [
    {
      "v": 1.0,
      "EventId": "bf50a49c34b74937a81e8d6fc95faa99",
      "ActionTaken": false
    }
  ],
  "Timestamp": "2021-02-04T16:31:29.9430000Z",
  "Version": "1",
  "EventId": "bf50a49c34b74937a81e8d6fc95faa99",
  "a": [1, 3, 2, 4],
  "c": {
    "FromUrl": [
      { "timeofday": "Evening", "weather": "Snowy", "name": "Alice" }
    ],
    "_multi": [
      {
        "_tag": "Cappucino",
        "i": { "constant": 1, "id": "Cappucino" },
        "j": [
          {
            "type": "hot",
            "origin": "kenya",
            "organic": "yes",
            "roast": "dark"
          }
        ]
      },
      {
        "_tag": "Cold brew",
        "i": { "constant": 1, "id": "Cold brew" },
        "j": [
          {
            "type": "cold",
            "origin": "brazil",
            "organic": "yes",
            "roast": "light"
          }
        ]
      },
      {
        "_tag": "Iced mocha",
        "i": { "constant": 1, "id": "Iced mocha" },
        "j": [
          {
            "type": "cold",
            "origin": "ethiopia",
            "organic": "no",
            "roast": "light"
          }
        ]
      },
      {
        "_tag": "Latte",
        "i": { "constant": 1, "id": "Latte" },
        "j": [
          {
            "type": "hot",
            "origin": "brazil",
            "organic": "no",
            "roast": "dark"
          }
        ]
      }
    ]
  },
  "p": [0.85, 0.05, 0.05, 0.05],
  "VWState": {
    "m": "ff0744c1aa494e1ab39ba0c78d048146/550c12cbd3aa47f09fbed3387fb9c6ec"
  },
  "_original_label_cost": -1.0
}
    """
    workspace = vw.Workspace(["--cb_explore_adf"])
    parser = vw.DSJsonFormatParser(workspace)
    result = parser.parse_json(text_input)
    assert len(result) == 5
    assert isinstance(result, list)


def test_reader() -> None:
    text_input = io.StringIO(
        """{"_label_cost":-0.0,"_label_probability":0.05000000074505806,"_label_Action":4,"_labelIndex":3,"o":[{"v":0.0,"EventId":"13118d9b4c114f8485d9dec417e3aefe","ActionTaken":false}],"Timestamp":"2021-02-04T16:31:29.2460000Z","Version":"1","EventId":"13118d9b4c114f8485d9dec417e3aefe","a":[4,2,1,3],"c":{"FromUrl":[{"timeofday":"Afternoon","weather":"Sunny","name":"Cathy"}],"_multi":[{"_tag":"Cappucino","i":{"constant":1,"id":"Cappucino"},"j":[{"type":"hot","origin":"kenya","organic":"yes","roast":"dark"}]},{"_tag":"Cold brew","i":{"constant":1,"id":"Cold brew"},"j":[{"type":"cold","origin":"brazil","organic":"yes","roast":"light"}]},{"_tag":"Iced mocha","i":{"constant":1,"id":"Iced mocha"},"j":[{"type":"cold","origin":"ethiopia","organic":"no","roast":"light"}]},{"_tag":"Latte","i":{"constant":1,"id":"Latte"},"j":[{"type":"hot","origin":"brazil","organic":"no","roast":"dark"}]}]},"p":[0.05,0.05,0.05,0.85],"VWState":{"m":"ff0744c1aa494e1ab39ba0c78d048146/550c12cbd3aa47f09fbed3387fb9c6ec"},"_original_label_cost":-0.0}
{"_label_cost":-1.0,"_label_probability":0.8500000238418579,"_label_Action":1,"_labelIndex":0,"o":[{"v":1.0,"EventId":"bf50a49c34b74937a81e8d6fc95faa99","ActionTaken":false}],"Timestamp":"2021-02-04T16:31:29.9430000Z","Version":"1","EventId":"bf50a49c34b74937a81e8d6fc95faa99","a":[1,3,2,4],"c":{"FromUrl":[{"timeofday":"Evening","weather":"Snowy","name":"Alice"}],"_multi":[{"_tag":"Cappucino","i":{"constant":1,"id":"Cappucino"},"j":[{"type":"hot","origin":"kenya","organic":"yes","roast":"dark"}]},{"_tag":"Cold brew","i":{"constant":1,"id":"Cold brew"},"j":[{"type":"cold","origin":"brazil","organic":"yes","roast":"light"}]},{"_tag":"Iced mocha","i":{"constant":1,"id":"Iced mocha"},"j":[{"type":"cold","origin":"ethiopia","organic":"no","roast":"light"}]},{"_tag":"Latte","i":{"constant":1,"id":"Latte"},"j":[{"type":"hot","origin":"brazil","organic":"no","roast":"dark"}]}]},"p":[0.85,0.05,0.05,0.05],"VWState":{"m":"ff0744c1aa494e1ab39ba0c78d048146/550c12cbd3aa47f09fbed3387fb9c6ec"},"_original_label_cost":-1.0}
{"_label_cost":-0.0,"_label_probability":0.05000000074505806,"_label_Action":2,"_labelIndex":1,"o":[{"v":0.0,"EventId":"a4460f60db7a4088a82a30728e9d4bab","ActionTaken":false}],"Timestamp":"2021-02-04T16:31:30.6530000Z","Version":"1","EventId":"a4460f60db7a4088a82a30728e9d4bab","a":[2,3,4,1],"c":{"FromUrl":[{"timeofday":"Morning","weather":"Sunny","name":"Bob"}],"_multi":[{"_tag":"Cappucino","i":{"constant":1,"id":"Cappucino"},"j":[{"type":"hot","origin":"kenya","organic":"yes","roast":"dark"}]},{"_tag":"Cold brew","i":{"constant":1,"id":"Cold brew"},"j":[{"type":"cold","origin":"brazil","organic":"yes","roast":"light"}]},{"_tag":"Iced mocha","i":{"constant":1,"id":"Iced mocha"},"j":[{"type":"cold","origin":"ethiopia","organic":"no","roast":"light"}]},{"_tag":"Latte","i":{"constant":1,"id":"Latte"},"j":[{"type":"hot","origin":"brazil","organic":"no","roast":"dark"}]}]},"p":[0.05,0.85,0.05,0.05],"VWState":{"m":"ff0744c1aa494e1ab39ba0c78d048146/550c12cbd3aa47f09fbed3387fb9c6ec"},"_original_label_cost":-0.0}
{"_label_cost":-1.0,"_label_probability":0.8500000238418579,"_label_Action":1,"_labelIndex":0,"o":[{"v":1.0,"EventId":"d8b78f0f016746d6b72e2889f0f58655","ActionTaken":false}],"Timestamp":"2021-02-04T16:31:31.1620000Z","Version":"1","EventId":"d8b78f0f016746d6b72e2889f0f58655","a":[1,4,3,2],"c":{"FromUrl":[{"timeofday":"Morning","weather":"Snowy","name":"Alice"}],"_multi":[{"_tag":"Cappucino","i":{"constant":1,"id":"Cappucino"},"j":[{"type":"hot","origin":"kenya","organic":"yes","roast":"dark"}]},{"_tag":"Cold brew","i":{"constant":1,"id":"Cold brew"},"j":[{"type":"cold","origin":"brazil","organic":"yes","roast":"light"}]},{"_tag":"Iced mocha","i":{"constant":1,"id":"Iced mocha"},"j":[{"type":"cold","origin":"ethiopia","organic":"no","roast":"light"}]},{"_tag":"Latte","i":{"constant":1,"id":"Latte"},"j":[{"type":"hot","origin":"brazil","organic":"no","roast":"dark"}]}]},"p":[0.85,0.05,0.05,0.05],"VWState":{"m":"ff0744c1aa494e1ab39ba0c78d048146/550c12cbd3aa47f09fbed3387fb9c6ec"},"_original_label_cost":-1.0}
{"_label_cost":-0.0,"_label_probability":0.8500000238418579,"_label_Action":1,"_labelIndex":0,"o":[{"v":0.0,"EventId":"1d9e9975f2274242bcc2d109674e09ac","ActionTaken":false}],"Timestamp":"2021-02-04T16:31:32.3270000Z","Version":"1","EventId":"1d9e9975f2274242bcc2d109674e09ac","a":[1,2,3,4],"c":{"FromUrl":[{"timeofday":"Morning","weather":"Sunny","name":"Alice"}],"_multi":[{"_tag":"Cappucino","i":{"constant":1,"id":"Cappucino"},"j":[{"type":"hot","origin":"kenya","organic":"yes","roast":"dark"}]},{"_tag":"Cold brew","i":{"constant":1,"id":"Cold brew"},"j":[{"type":"cold","origin":"brazil","organic":"yes","roast":"light"}]},{"_tag":"Iced mocha","i":{"constant":1,"id":"Iced mocha"},"j":[{"type":"cold","origin":"ethiopia","organic":"no","roast":"light"}]},{"_tag":"Latte","i":{"constant":1,"id":"Latte"},"j":[{"type":"hot","origin":"brazil","organic":"no","roast":"dark"}]}]},"p":[0.85,0.05,0.05,0.05],"VWState":{"m":"ff0744c1aa494e1ab39ba0c78d048146/550c12cbd3aa47f09fbed3387fb9c6ec"},"_original_label_cost":-0.0}
{"_label_cost":-0.0,"_label_probability":0.8500000238418579,"_label_Action":4,"_labelIndex":3,"o":[{"v":0.0,"EventId":"ea6be41bc1b04eb89befdce03f3fe3a1","ActionTaken":false}],"Timestamp":"2021-02-04T16:31:32.9270000Z","Version":"1","EventId":"ea6be41bc1b04eb89befdce03f3fe3a1","a":[4,1,3,2],"c":{"FromUrl":[{"timeofday":"Evening","weather":"Rainy","name":"Cathy"}],"_multi":[{"_tag":"Cappucino","i":{"constant":1,"id":"Cappucino"},"j":[{"type":"hot","origin":"kenya","organic":"yes","roast":"dark"}]},{"_tag":"Cold brew","i":{"constant":1,"id":"Cold brew"},"j":[{"type":"cold","origin":"brazil","organic":"yes","roast":"light"}]},{"_tag":"Iced mocha","i":{"constant":1,"id":"Iced mocha"},"j":[{"type":"cold","origin":"ethiopia","organic":"no","roast":"light"}]},{"_tag":"Latte","i":{"constant":1,"id":"Latte"},"j":[{"type":"hot","origin":"brazil","organic":"no","roast":"dark"}]}]},"p":[0.85,0.05,0.05,0.05],"VWState":{"m":"ff0744c1aa494e1ab39ba0c78d048146/550c12cbd3aa47f09fbed3387fb9c6ec"},"_original_label_cost":-0.0}
{"_label_cost":-0.0,"_label_probability":0.8500000238418579,"_label_Action":3,"_labelIndex":2,"o":[{"v":0.0,"EventId":"2c53de8bf44749789d205b101025f7af","ActionTaken":false}],"Timestamp":"2021-02-04T16:31:33.6460000Z","Version":"1","EventId":"2c53de8bf44749789d205b101025f7af","a":[3,2,1,4],"c":{"FromUrl":[{"timeofday":"Afternoon","weather":"Sunny","name":"Cathy"}],"_multi":[{"_tag":"Cappucino","i":{"constant":1,"id":"Cappucino"},"j":[{"type":"hot","origin":"kenya","organic":"yes","roast":"dark"}]},{"_tag":"Cold brew","i":{"constant":1,"id":"Cold brew"},"j":[{"type":"cold","origin":"brazil","organic":"yes","roast":"light"}]},{"_tag":"Iced mocha","i":{"constant":1,"id":"Iced mocha"},"j":[{"type":"cold","origin":"ethiopia","organic":"no","roast":"light"}]},{"_tag":"Latte","i":{"constant":1,"id":"Latte"},"j":[{"type":"hot","origin":"brazil","organic":"no","roast":"dark"}]}]},"p":[0.85,0.05,0.05,0.05],"VWState":{"m":"ff0744c1aa494e1ab39ba0c78d048146/550c12cbd3aa47f09fbed3387fb9c6ec"},"_original_label_cost":-0.0}
{"_label_cost":-1.0,"_label_probability":0.8500000238418579,"_label_Action":3,"_labelIndex":2,"o":[{"v":1.0,"EventId":"cea16d42810c41429e6a2c468769f70c","ActionTaken":false}],"Timestamp":"2021-02-04T16:31:34.1620000Z","Version":"1","EventId":"cea16d42810c41429e6a2c468769f70c","a":[3,1,4,2],"c":{"FromUrl":[{"timeofday":"Afternoon","weather":"Snowy","name":"Bob"}],"_multi":[{"_tag":"Cappucino","i":{"constant":1,"id":"Cappucino"},"j":[{"type":"hot","origin":"kenya","organic":"yes","roast":"dark"}]},{"_tag":"Cold brew","i":{"constant":1,"id":"Cold brew"},"j":[{"type":"cold","origin":"brazil","organic":"yes","roast":"light"}]},{"_tag":"Iced mocha","i":{"constant":1,"id":"Iced mocha"},"j":[{"type":"cold","origin":"ethiopia","organic":"no","roast":"light"}]},{"_tag":"Latte","i":{"constant":1,"id":"Latte"},"j":[{"type":"hot","origin":"brazil","organic":"no","roast":"dark"}]}]},"p":[0.85,0.05,0.05,0.05],"VWState":{"m":"ff0744c1aa494e1ab39ba0c78d048146/550c12cbd3aa47f09fbed3387fb9c6ec"},"_original_label_cost":-1.0}
{"_label_cost":-1.0,"_label_probability":0.8500000238418579,"_label_Action":1,"_labelIndex":0,"o":[{"v":1.0,"EventId":"2dfd60f5f47a451fbe7f674afc5cafd7","ActionTaken":false}],"Timestamp":"2021-02-04T16:31:35.3180000Z","Version":"1","EventId":"2dfd60f5f47a451fbe7f674afc5cafd7","a":[1,3,4,2],"c":{"FromUrl":[{"timeofday":"Afternoon","weather":"Snowy","name":"Dave"}],"_multi":[{"_tag":"Cappucino","i":{"constant":1,"id":"Cappucino"},"j":[{"type":"hot","origin":"kenya","organic":"yes","roast":"dark"}]},{"_tag":"Cold brew","i":{"constant":1,"id":"Cold brew"},"j":[{"type":"cold","origin":"brazil","organic":"yes","roast":"light"}]},{"_tag":"Iced mocha","i":{"constant":1,"id":"Iced mocha"},"j":[{"type":"cold","origin":"ethiopia","organic":"no","roast":"light"}]},{"_tag":"Latte","i":{"constant":1,"id":"Latte"},"j":[{"type":"hot","origin":"brazil","organic":"no","roast":"dark"}]}]},"p":[0.85,0.05,0.05,0.05],"VWState":{"m":"ff0744c1aa494e1ab39ba0c78d048146/550c12cbd3aa47f09fbed3387fb9c6ec"},"_original_label_cost":-1.0}
{"_label_cost":-1.0,"_label_probability":0.8500000238418579,"_label_Action":4,"_labelIndex":3,"o":[{"v":1.0,"EventId":"9c21eb678a234fb781d9b57541a8ee4d","ActionTaken":false}],"Timestamp":"2021-02-04T16:31:35.9220000Z","Version":"1","EventId":"9c21eb678a234fb781d9b57541a8ee4d","a":[4,1,3,2],"c":{"FromUrl":[{"timeofday":"Afternoon","weather":"Rainy","name":"Cathy"}],"_multi":[{"_tag":"Cappucino","i":{"constant":1,"id":"Cappucino"},"j":[{"type":"hot","origin":"kenya","organic":"yes","roast":"dark"}]},{"_tag":"Cold brew","i":{"constant":1,"id":"Cold brew"},"j":[{"type":"cold","origin":"brazil","organic":"yes","roast":"light"}]},{"_tag":"Iced mocha","i":{"constant":1,"id":"Iced mocha"},"j":[{"type":"cold","origin":"ethiopia","organic":"no","roast":"light"}]},{"_tag":"Latte","i":{"constant":1,"id":"Latte"},"j":[{"type":"hot","origin":"brazil","organic":"no","roast":"dark"}]}]},"p":[0.85,0.05,0.05,0.05],"VWState":{"m":"ff0744c1aa494e1ab39ba0c78d048146/550c12cbd3aa47f09fbed3387fb9c6ec"},"_original_label_cost":-1.0}"""
    )
    workspace = vw.Workspace(["--cb_explore_adf"])
    counter = 0
    with vw.DSJsonFormatReader(workspace, text_input) as reader:
        for example in reader:
            # perform assert example is not a list
            counter += 1
            assert isinstance(example, list)
            assert len(example) == 5

    assert counter == 10
