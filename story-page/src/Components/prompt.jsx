import { Button } from '@mui/material';
import Box from '@mui/material/Box';
import TextField from '@mui/material/TextField';
const Prompt = () =>{
    return (
        <div style={{position:'fixed' , bottom:0, width:'100%',  display: 'flex', justifyContent: 'center', alignItems:'center', marginBottom:'10px'}}>
        
                <Box
                    sx={{
                        width: '90%',
                        maxWidth: '100%',
                    }}
                    >
                    <TextField fullWidth label="Prompt" id="fullWidth" style={{background:'#fff' , color:'#fff'}} />
                
                </Box>
                <Button  variant="contained" style={{height:'56px'}} >
                        Submit
                </Button>
 
        </div>
    );
}

export default Prompt;