# Python flask cookbook API

Small really basic flask API

## Installation

```bash
python3 -m venv dev
source dev/bin/activate
pip3 install requirements.txt
```

## Usage

### GET
http://localhost:5000/recipes

### POST
```json
{
	"title": "Sandwich",
	"description": "Classical sandwitch ",
	"ingredients": [ 
	   {
	       "name": "cheese",
	       "quantity": "5g0"
	   },
	   {
	       "name": "bread",
	       "quantity": "150g"
	   },
	   {
	       "name": "ham",
	       "quantity": "50g"
	   }
	]
}
```


## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
None