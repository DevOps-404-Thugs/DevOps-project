import React from 'react';
import { BrowserRouter } from 'react-router-dom';
import renderer from 'react-test-renderer';
import Account from './Account';


describe('Account component', () =>{
    test("match the snapshot", () =>{
        const component = renderer.create(
            <BrowserRouter>
                <Account/>
            </BrowserRouter>
        );
        let tree = component.toJSON();
        expect(tree).toMatchSnapshot();
    });  
});