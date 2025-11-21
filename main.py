from server import create_mcp_server  
  
def main():
    mcp = create_mcp_server()
    mcp.run(transport='streamable-http')    

if __name__ == "__main__":
    main()
