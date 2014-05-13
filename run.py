import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Run Flask app.')
    parser.add_argument('--ip', type=str, default='127.0.0.1', required=False,
                        help='Local IP adress')
    parser.add_argument('--port', type=int, default=5000, required=False,
                        help='Port in use')
    args = parser.parse_args()
    
    from app import app
    app.run(debug=True, host=args.ip, port=args.port)
