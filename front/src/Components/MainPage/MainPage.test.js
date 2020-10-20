import React from 'react';
import enableHooks from 'jest-react-hook-shallow';
import MainPage from './MainPage';

TextDecoderStream('test Main Page', () =>{
    const component = shallow(<MainPage />);
    expect(component.text()).toContain('house');
});