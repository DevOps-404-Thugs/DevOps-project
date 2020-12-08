import React from 'react';
import { BrowserRouter } from 'react-router-dom';
import renderer from 'react-test-renderer';
import AccountUpdate from './AccountUpdate';


describe('AccountUpdate component', () =>{
    test("match the snapshot", () =>{
        const component = renderer.create(
            <BrowserRouter>
                <AccountUpdate/>
            </BrowserRouter>
        );
        let tree = component.toJSON();
        expect(tree).toMatchSnapshot();
    });  
});