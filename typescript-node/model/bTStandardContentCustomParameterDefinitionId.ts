/**
 * Onshape REST API
 * The Onshape REST API consumed by all clients.
 *
 * OpenAPI spec version: 1.93
 * Contact: api-support@onshape.zendesk.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */


export class BTStandardContentCustomParameterDefinitionId {
    'propertyId'?: string;
    'ownerId'?: string;
    'ownerType'?: number;
    'parameterName'?: string;
    'standard'?: string;
    'category'?: string;
    'types'?: string;
    'type'?: string;

    static discriminator: string | undefined = undefined;

    static attributeTypeMap: Array<{name: string, baseName: string, type: string}> = [
        {
            "name": "propertyId",
            "baseName": "propertyId",
            "type": "string"
        },
        {
            "name": "ownerId",
            "baseName": "ownerId",
            "type": "string"
        },
        {
            "name": "ownerType",
            "baseName": "ownerType",
            "type": "number"
        },
        {
            "name": "parameterName",
            "baseName": "parameterName",
            "type": "string"
        },
        {
            "name": "standard",
            "baseName": "standard",
            "type": "string"
        },
        {
            "name": "category",
            "baseName": "category",
            "type": "string"
        },
        {
            "name": "types",
            "baseName": "types",
            "type": "string"
        },
        {
            "name": "type",
            "baseName": "type",
            "type": "string"
        }    ];

    static getAttributeTypeMap() {
        return BTStandardContentCustomParameterDefinitionId.attributeTypeMap;
    }
}
