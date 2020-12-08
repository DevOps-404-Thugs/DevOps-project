import React from 'react';
import { BrowserRouter } from 'react-router-dom';
import renderer from 'react-test-renderer';
import Upload from './Upload';


describe('Upload component', () =>{
    test("match the snapshot", () =>{
        const component = renderer.create(
            <BrowserRouter>
                <Upload/>
            </BrowserRouter>
        );
        let tree = component.toJSON();
        expect(tree).toMatchSnapshot();
    });  
});