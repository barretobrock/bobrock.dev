import React from 'react';


const Footer = () => {
    let d = new Date();

    return (
        <footer>
            <p className={'copyright'}>©{d.getFullYear()} Barret Obrock</p>
        </footer>
    )
};

export default Footer;
