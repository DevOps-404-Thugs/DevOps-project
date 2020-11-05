import React from 'react';
import renderer from 'react-test-renderer';
import {Description} from './Detail.js';

test('Description generates correct page', () => {
    const component = renderer.create(
        <Description objectId="123" />
    );
    let tree = component.toJSON();
    expect(tree).toMatchSnapshot();
});

