import { Box, Tab, Tabs } from "@mui/material";
import React from "react";



export default function AdmPage() {
    const [value, setValue] = React.useState(0);

    function a11yProps(index) {
        return {
            id: `simple-tab-${index}`,
            'aria-controls': `simple-tabpanel-${index}`,
        };
    }

    return (
        <Box {...{ sx: { marginTop: 25, marginLeft: 80, width: "100%" } }}>
            <Tabs value={value} onChange={(event, newValue) => { setValue(newValue); }} aria-label="basic tabs example">
                <Tab label="Item One" {...a11yProps(0)} />
                <Tab label="Item Two" {...a11yProps(1)} />
                <Tab label="Item Three" {...a11yProps(2)} />
            </Tabs>
        </Box>
    );
}